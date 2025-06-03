MAIN_ANALYSIS_PY = '''
"""
TOLARAM DATA SCIENTIST ASSESSMENT
==================================

Main analysis script for the 24-hour assessment project.
"""

import sys
import os

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import the SAP analytics package
from sap_analytics import run_complete_tolaram_assessment

def main():
    """
    Main function for Tolaram assessment
    """
    print("🎯 TOLARAM DATA SCIENTIST ASSESSMENT")
    print("=" * 60)
    print("Starting comprehensive SAP manufacturing analysis...")
    
    # Path to your assessment data
    data_file = "data/Project_Assessment_Data.xlsx"
    
    # Check if file exists
    if not os.path.exists(data_file):
        print(f"❌ Data file not found: {data_file}")
        print("Please ensure the Excel file is in the data/ folder")
        return
    
    try:
        # Run complete assessment
        results = run_complete_tolaram_assessment(
            data_file_path=data_file,
            result_folder="tolaram_results"
        )
        
        # Print summary for quick review
        print("\\n📋 ASSESSMENT SUMMARY:")
        print("=" * 40)
        
        summary = results['assessment_summary']
        print(f"• Total Orders Analyzed: {summary['data_overview']['total_orders']:,}")
        print(f"• Plants Analyzed: {summary['data_overview']['plants_analyzed']}")
        print(f"• ML Models Developed: {summary['ml_insights'].get('models_developed', 0)}")
        print(f"• Bottlenecks Identified: {summary['bottleneck_insights'].get('bottlenecks_identified', 0)}")
        print(f"• Visualizations Created: {len(results['visualizations'].get('created_files', []))}")
        
        print("\\n🎯 KEY FINDINGS:")
        for finding in summary['key_findings'][:5]:
            print(f"  • {finding}")
        
        print("\\n💡 TOP RECOMMENDATIONS:")
        for rec in summary['recommendations'][:3]:
            print(f"  • {rec}")
        
        print(f"\\n📁 Results saved to: {results['session_folder']}")
        print("\\n✅ Assessment completed successfully!")
        
        return results
        
    except Exception as e:
        print(f"❌ Assessment failed: {e}")
        raise e

if __name__ == "__main__":
    results = main()
'''