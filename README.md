

# Tolaram Africa Enterprises - Manufacturing Operations Analysis

This repository contains a comprehensive data science assessment project for **Tolaram Africa Enterprises**, focusing on **manufacturing operations analysis and optimization**.

---

## Project Overview

Our goal in this project is to analyze and improve key aspects of manufacturing operations by leveraging data from SAP ERP systems. This analysis aims to drive operational efficiency, enhance quality control, and optimize overall performance across multiple manufacturing plants.

### 🎯 Project Objectives

* **Identify operational inefficiencies** across production and quality management systems.
* **Analyze quality issues and patterns** that impact manufacturing performance.
* **Develop predictive models** for proactive quality management.
* **Provide actionable recommendations** for operational excellence.
* **Quantify business impact and ROI** of proposed improvements.

---

## 📊 Data Sources

We're using 13 SAP manufacturing datasets, covering various aspects of production and quality management from the SAP ERP system:

### Production Planning (PP) Module

* **AUFK**: Order Master Data (production order headers)
* **AFKO**: Order Header Data (scheduling and planning)
* **AFPO**: Order Items (production order line items)
* **AUFM**: Goods Movements (material movements and consumption)

### Quality Management (QM) Module

* **QMEL**: Quality Notifications (quality issues and alerts)
* **QMFE**: Quality Defects (specific defect records)
* **QMUR**: Quality Causes (root cause analysis)
* **QMIH**: Maintenance Notifications (quality-related maintenance)

### Master Data & Support Tables

* **Plant Description**: Manufacturing plant master data
* **crhd_v1**: Work Centers (manufacturing work centers)
* **JEST**: Status Information (object status tracking)
* **QPCD**: Quality Codes (quality classification codes)
* **QPCT**: Quality Code Texts (code descriptions)
* **QPGT**: Quality Group Texts (code group descriptions)

---

## 🪠 Entity Relationship Diagram (ERD)

This diagram visualizes the connections between the SAP tables used in our analysis, showing how different data points relate across production, quality management, and master data modules.


**🪠 ERD (Entity Relationship Diagram)**
This Entity-Relationship Diagram visualizes the connections between the key SAP tables used in this analysis, illustrating how different data points relate to each other across production and quality management modules.


```mermaid 
    graph TB
    %% Production Planning Tables
    subgraph PP ["🏭 Production Planning"]
        AUFK["📋 AUFK<br/>Order Master<br/>AUFNR, WERKS, AUART"]
        AFKO["📅 AFKO<br/>Order Header<br/>AUFNR, Scheduling"]
        AFPO["📦 AFPO<br/>Order Items<br/>AUFNR, PWERK, MATNR"]
        AUFM["📊 AUFM<br/>Goods Movements<br/>AUFNR, WERKS, MENGE"]
    end

    %% Quality Management Tables
    subgraph QM ["🔍 Quality Management"]
        QMEL["🚨 QMEL<br/>Quality Notifications<br/>QMNUM, AUFNR, QMGRP+QMCOD"]
        QMFE["⚠️ QMFE<br/>Quality Defects<br/>QMNUM, FENUM, FEGRP+FECOD"]
        QMUR["🎯 QMUR<br/>Root Causes<br/>QMNUM, FENUM, URGRP+URCOD"]
        QMIH["🔧 QMIH<br/>Maintenance Notifications<br/>QMNUM, ABNUM, EQUNR"]
    end

    %% Code Definition Tables
    subgraph CODES ["📚 Code Definitions"]
        QPCD["📖 QPCD<br/>Code Definitions<br/>KATALOGART+CODEGRUPPE+CODE"]
        QPCT["📝 QPCT<br/>Code Texts<br/>KURZTEXT, LTEXTV"]
        QPGT["📂 QPGT<br/>Group Texts<br/>CODEGRUPPE Descriptions"]
    end

    %% Master Data Tables
    subgraph MD ["🏢 Master Data"]
        PLANT["🏭 Plant Description<br/>Plant_Code: A110-A810<br/>Plant_Name"]
        CRHD["⚙️ CRHD_V1<br/>Work Centers<br/>ARBPL, WERKS, KTEXT"]
        JEST["📊 JEST<br/>Status Information<br/>OBJNR, STAT"]
    end

    %% Main Integration Flow - Production Orders
    AUFK -->|AUFNR| AFKO
    AUFK -->|AUFNR| AFPO
    AUFK -->|AUFNR| AUFM

    %% Plant Linkages (Multiple Sources)
    AUFK -->|WERKS| PLANT
    AFPO -->|PWERK| PLANT
    AUFM -->|WERKS| PLANT
    CRHD -->|WERKS| PLANT

    %% Quality Integration Chain
    AUFK -->|AUFNR| QMEL
    QMEL -->|QMNUM| QMFE
    QMFE -->|QMNUM+FENUM| QMUR
    QMEL -->|QMNUM| QMIH

    %% Code Description Chain
    QMEL -->|QMGRP+QMCOD| QPCD
    QMFE -->|FEGRP+FECOD| QPCD
    QMUR -->|URGRP+URCOD| QPCD
    QPCD -->|KATALOGART+CODEGRUPPE+CODE| QPCT
    QPCD -->|KATALOGART+CODEGRUPPE| QPGT

    %% Work Center Integration
    AFKO -->|ARBPL_OBJID| CRHD
    QMFE -->|ARBPL| CRHD
    QMIH -->|WARPL| CRHD

    %% Status Integration
    AUFK -->|OBJNR| JEST
    QMEL -->|OBJNR| JEST

    %% Additional Quality Links
    AFPO -->|QUNUM| QMEL
    AFPO -->|CHARG| QMFE
    AUFM -->|CHARG| QMFE

    %% Custom Order Fields
    QMEL -.->|ZZAUFNR1-10| AUFK
    QMIH -->|ABNUM| AUFK

    %% Styling with black text
    classDef production fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#000000
    classDef quality fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#000000
    classDef codes fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000000
    classDef master fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px,color:#000000

    class AUFK,AFKO,AFPO,AUFM production
    class QMEL,QMFE,QMUR,QMIH quality
    class QPCD,QPCT,QPGT codes
    class PLANT,CRHD,JEST master
```


**🧰 Technical Implementation**

Requirements

-Ensure you have the necessary Python libraries installed.

```bash 
pip install pandas numpy matplotlib seaborn plotly scikit-learn openpyxl scipy
```
## Tools & Techniques

- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)

- Data cleaning, feature engineering, and KPI tracking

## Deliverables

- Insightful dashboards and reports

- Anomaly detection in production workflows

- Predictive models for bottleneck and defect trends

- Actionable recommendations for operational improvement

---
**📄 License**
This project is created as part of a data science assessment for Tolaram Africa Enterprises. 
All code and analysis are provided for evaluation purposes only.

**🙏 Acknowledgments**
We extend our gratitude to:

-Tolaram Africa Enterprises for providing this valuable opportunity.

-The SAP Community for extensive documentation and support.

**Author:** Olayinka Akerekan  

**Date:** June 2025

**Project Type:** Data Science Assessment
