```mermaid
erDiagram
    %% Order Master Data
    AUFK {
        string MANDT PK
        string AUFNR PK "Order Number"
        string AUART "Order Type"
    }
    
    %% PP Order Header
    AFKO {
        string MANDT PK
        string AUFNR PK "Order Number"
        string ARBPL_OBJID FK "Work Center Object ID (to CRHD_V1.OBJID)"
    }
    
    %% PP Order Item
    AFPO {
        string MANDT PK
        string AUFNR PK "Order Number"
        string POSNR PK "Item Number"
        string MATNR "Material Number"
        string CHARG "Batch Number"
    }
    
    %% Goods Movements
    AUFM {
        string MANDT PK
        string MBLNR PK "Material Doc No"
        string MJAHR PK "Material Doc Year"
        string ZEILE PK "Doc Item"
        string AUFNR FK "Order Number (to AFKO.AUFNR)"
        string MATNR "Material Number"
        string BWART "Movement Type"
        string CHARG "Batch Number"
    }
    
    %% Quality Notification Header
    QMEL {
        string MANDT PK
        string QMNUM PK "Quality Notification No"
        string QMART "Notif. Type (Quality)"
        string AUFNR FK "Order Number (to AFKO.AUFNR)"
        string QMGRP "Code Group (Hdr)"
        string QMCOD "Code (Hdr)"
    }
    
    %% Quality Notification Defects/Items
    QMFE {
        string MANDT PK
        string QMNUM PK "Quality Notif. No (to QMEL.QMNUM)"
        string FENUM PK "Defect Sequence No"
        string FEKAT FK "Defect Catalog Type (to QPCD.KATALOGART)"
        string FEGRP FK "Defect Group (to QPCD.CODEGRUPPE)"
        string FECOD FK "Defect Code (to QPCD.CODE)"
        string FERTAUFNR "Prod. Order (Defect)"
    }
    
    %% Quality Notification Causes
    QMUR {
        string MANDT PK
        string QMNUM PK "Quality Notif. No (to QMEL.QMNUM)"
        string FENUM PK "Defect Sequence No (to QMFE.FENUM)"
        string URNUM PK "Cause Sequence No"
        string URKAT FK "Cause Catalog Type (to QPCD.KATALOGART)"
        string URGRP FK "Cause Group (to QPCD.CODEGRUPPE)"
        string URCOD FK "Cause Code (to QPCD.CODE)"
        boolean ROOTCAUSE "Root Cause Indicator"
    }
    
    %% Maintenance Notification Header
    QMIH {
        string MANDT PK
        string QMNUM PK "Maintenance Notification No"
        string ILART "Notif. Type (Maint.)"
        string EQUNR "Equipment Number"
        string ABNUM FK "Maint. Order No (to AUFK.AUFNR)"
        string DETECTIONCATALOG FK "Detect. Catalog (to QPCD.KATALOGART)"
        string DETECTIONCODEGROUP FK "Detect. Code Grp (to QPCD.CODEGRUPPE)"
        string DETECTIONCODE FK "Detect. Code (to QPCD.CODE)"
    }
    
    %% Code Group Texts
    QPGT {
        string MANDANT PK
        string KATALOGART PK "Catalog Type"
        string CODEGRUPPE PK "Code Group"
        string SPRACHE PK "Language"
        string KURZTEXT "Short Text for Group"
    }
    
    %% Catalog Code Definitions
    QPCD {
        string MANDT PK
        string KATALOGART PK "Catalog Type (to QPGT.KATALOGART)"
        string CODEGRUPPE PK "Code Group (to QPGT.CODEGRUPPE)"
        string CODE PK "Code"
        string VERSION PK "Version"
        date GUELTIGAB "Valid From Date"
        string FEHLKLASSE "Error Class"
        boolean INAKTIV "Inactive Indicator"
        string FOLGEAKTI "Follow-Up Action"
    }
    
    %% Work Center Header Data
    CRHD_V1 {
        string MANDT PK "Client - SAP client number"
        string OBJTY PK "Object Type - Type of object"
        string OBJID PK "Object ID - Unique identifier"
        string SPRAS PK "Language Key"
        string ARBPL "Work Center - Work center identifier"
        string WERKS "Plant - Plant where work center is located"
        string KTEXT "Short Description - Name of work center"
    }
    
    %% Object Status Information
    JEST {
        string MANDT PK "Client - SAP client number"
        string OBJNR PK "Object Number - Unique identifier"
        string STAT PK "Status - Status code"
        string INACT "Inactive Indicator"
        string CHGNR "Change Number"
        string _DATAAGING "Data Aging - Historical data flag"
    }
    
    %% Plant Master Data
    T001W {
        string MANDT PK "Client - SAP client number"
        string WERKS PK "Plant Code"
        string NAME1 "Plant Name"
    }
    
    %% Catalog Code Descriptions
    QPCT {
        string MANDT PK "Client - SAP client number"
        string KATALOGART PK "Catalog Type - Type of catalog"
        string CODEGRUPPE PK "Code Group - Group of codes within catalog"
        string CODE PK "Code - Specific code for defect/cause/action"
        string SPRACHE PK "Language - Language key for description"
        string VERSION PK "Version - Version number of the code"
        date GUELTIGAB "Valid From Date - Date from which code is valid"
        string KURZTEXT "Short Text - Short description of the code"
        string LTEXTV "Long Text - Detailed description of the code"
        boolean INAKTIV "Inactive Indicator - Marks code as inactive"
        boolean GELOESCHT "Deletion Indicator - Marks code for deletion"
    }
    
    %% Relationships
    AUFK ||--|| AFKO : "general_to_pp_specific"
    AUFK ||--o{ QMIH : "is_maint_notif_for_order"
    AFKO ||--|{ AFPO : "contains_items"
    AFKO ||--o{ QMEL : "has_quality_notifications"
    AFKO ||--o{ AUFM : "has_goods_movements"
    AFKO }o--|| CRHD_V1 : "uses_work_center"
    CRHD_V1 }o--|| T001W : "located_in_plant"
    QMEL ||--|{ QMFE : "details_defect_items"
    QMFE ||--o{ QMUR : "has_causes"
    QPGT ||--o{ QPCD : "defines_codes_for_group"
    QPCD ||--o{ QPCT : "has_code_descriptions"
    QMEL }o--|| QPCD : "uses_hdr_code"
    QMFE }o--|| QPCD : "uses_defect_code"
    QMUR }o--|| QPCD : "uses_cause_code"
    QMIH }o--|| QPCD : "uses_detection_code"