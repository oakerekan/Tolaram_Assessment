import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score, pairwise_distances
import matplotlib.pyplot as plt
from ace_tools import display_dataframe_to_user

# 1. Load dataset with correct date parsing
df = pd.read_excel(r"C:\Users\pbrin\Downloads\DATA WIP SORTED BASED ON ACTIVE STATE.xlsx",
                   parse_dates=['Start Datetime', 'End Datetime'])
print(f"Dataset shape: {df.shape}")

# 2. Clean & classify
df_clean = df.dropna(subset=['Start Datetime', 'End Datetime']).copy()
df_clean['is_active'] = np.where(df_clean['Stoppage Category'] == 'Not Occupied', 0, 1)

# 3. Generate summary statistical features per group
grouped = df_clean.groupby(['Line', 'Stoppage Reason', 'Shift Id'])
stats = pd.DataFrame({
    'mean': grouped['Bottleneck Duration Seconds'].mean(),
    'std': grouped['Bottleneck Duration Seconds'].std(),
    'max': grouped['Bottleneck Duration Seconds'].max(),
    'min': grouped['Bottleneck Duration Seconds'].min(),
    'count': grouped['Bottleneck Duration Seconds'].count()
}).dropna()

print(f"Number of groups for clustering: {stats.shape[0]}")

# 4. Scale features
scaler = StandardScaler()
X_feat = scaler.fit_transform(stats)

# 5. Compute Euclidean distance matrix
D = pairwise_distances(X_feat, metric='euclidean')

# 6. Agglomerative Hierarchical Clustering
n_clusters = 4
Z = linkage(D, method='complete')
ahc = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='complete')
labels_ahc = ahc.fit_predict(D)

# 7. Density-based clustering via DBSCAN (proxy for HDBSCAN)
eps = np.median(D)
dbscan = DBSCAN(eps=eps, min_samples=5, metric='precomputed')
labels_db = dbscan.fit_predict(D)

# 8. Compute evaluation metrics
metrics = []
for name, labels in [('AHC', labels_ahc), ('DBSCAN', labels_db)]:
    # Silhouette
    sil = silhouette_score(D, labels, metric='precomputed') if len(set(labels)) > 1 else np.nan
    mask = labels >= 0
    # Davies-Bouldin and Calinski-Harabasz on feature space
    if len(set(labels[mask])) > 1:
        db = davies_bouldin_score(X_feat[mask], labels[mask])
        ch = calinski_harabasz_score(X_feat[mask], labels[mask])
    else:
        db, ch = (np.nan, np.nan)
    metrics.append({
        'Algorithm': name,
        'Silhouette': sil,
        'Davies-Bouldin': db,
        'Calinski-Harabasz': ch
    })

metrics_df = pd.DataFrame(metrics).set_index('Algorithm')

# 9. Display metrics
display_dataframe_to_user('Clustering Performance Metrics', metrics_df)

# 10. Plot dendrogram for AHC
plt.figure(figsize=(10, 5))
dendrogram(Z, color_threshold=0)
plt.title('Dendrogram: Agglomerative Hierarchical Clustering')
plt.xlabel('Group index')
plt.ylabel('Euclidean Distance')
plt.show()

# 11. Print cluster counts
print('AHC cluster counts:', np.bincount(labels_ahc))
print('DBSCAN cluster counts (including noise as -1):', np.bincount(labels_db + 1))
