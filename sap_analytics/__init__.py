SAP_ANALYTICS_INIT = '''
"""
SAP Analytics Package
=====================

Comprehensive SAP manufacturing and quality management analytics suite.
"""

__version__ = "1.0.0"
__author__ = "Tolaram Assessment"

# Import main classes for easy access
from .core.data_integration import create_comprehensive_sap_view
from .core.data_validation import run_complete_validation_suite
from .ml.ml_analytics import run_complete_ml_analysis
from .ml.bottleneck_detection import run_complete_bottleneck_analysis
from .visualization.viz_suite import create_complete_visualization_suite
from .utils.results_manager import run_complete_analysis_with_results_folder

# Main workflow function
from .workflows import run_complete_tolaram_assessment

__all__ = [
    'create_comprehensive_sap_view',
    'run_complete_validation_suite', 
    'run_complete_ml_analysis',
    'run_complete_bottleneck_analysis',
    'create_complete_visualization_suite',
    'run_complete_analysis_with_results_folder',
    'run_complete_tolaram_assessment'
]
'''