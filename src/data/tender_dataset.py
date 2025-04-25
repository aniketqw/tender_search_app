TENDER_DATASET = {
    "websites": [
        {
            "name": "Global Tenders",
            "base_url": "globaltenders.com",
            "specializations": ["construction", "IT", "healthcare"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily"
            }
        },
        {
            "name": "Tender Impulse",
            "base_url": "tenderimpulse.com",
            "specializations": ["government", "public_procurement"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily"
            }
        }
    ],
    "keywords_mapping": {
        "construction": ["building", "infrastructure", "civil_works"],
        "IT": ["software", "hardware", "digital"],
        "healthcare": ["medical", "hospital", "pharmaceutical"]
    }
}
