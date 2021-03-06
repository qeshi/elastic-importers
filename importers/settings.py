import os

ES_HOST = os.getenv("ES_HOST", "localhost")
ES_PORT = os.getenv("ES_PORT", 9200)
ES_USER = os.getenv("ES_USER")
ES_PWD = os.getenv("ES_PWD")

# For platsannonser
ES_ANNONS_INDEX = os.getenv('ES_ANNONS_INDEX', os.getenv('ES_ANNONS', 'platsannons'))
platsannons_mappings = {
    "mappings": {
        "document": {
            "properties": {
                "complete": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "keywords": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "publiceringsdatum": {
                    "type": "date"
                },
                "sista_ansokningsdatum": {
                    "type": "date"
                },
                "status": {
                    "properties": {
                        "sista_publiceringsdatum": {
                            "type": "date"
                        },
                        "skapad": {
                            "type": "date"
                        },
                        "uppdaterad": {
                            "type": "date"
                        },
                    }
                },
                "arbetsplatsadress": {
                    "properties": {
                        "kommunkod": {
                            "type": "text"
                        },
                        "coordinates": {
                            "type": "geo_point",
                            "ignore_malformed": True
                        }
                    }
                },
                "arbetsomfattning": {
                    "properties": {
                        "min": {
                            "type": "float"
                        },
                        "max": {
                            "type": "float"
                        }
                    }
                }
            }
        }
    }
}

# For postgres (platsannonser and auranest)
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT", 5432)
PG_DBNAME = os.getenv("PG_DBNAME")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_BATCH_SIZE = os.getenv("PG_BATCH_SIZE", 1000)

# For kandidat import
ES_KANDIDAT_INDEX = os.getenv('ES_KANDIDAT_INDEX', os.getenv('ES_KANDIDAT', 'kandidater'))
ORACLE_USER = os.getenv('ORACLE_USER')
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD')
ORACLE_PORT = os.getenv('ORACLE_PORT', '1521')
ORACLE_HOST = os.getenv('ORACLE_HOST')
ORACLE_SERVICE = os.getenv('ORACLE_SERVICE')

# For auranest import
ES_AURANEST_INDEX = os.getenv('ES_AURANEST_INDEX', os.getenv('ES_AURANEST', 'auranest'))
ES_ONTOLOGY_INDEX = os.getenv('ES_ONTOLOGY_INDEX', os.getenv('ES_ONTOLOGY', 'ontology'))

auranest_mappings = {
    "settings": {
        "analysis": {
            "normalizer": {
                "lc_normalizer": {
                    "type": "custom",
                    "filter": ["lowercase"]
                }
            }
        }
    },
    "mappings": {
        "document": {
            "properties": {
                "id": {
                    "type": "keyword"
                },
                "group": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "keyword"
                        }
                    }
                },
                "skills": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "copy_to": "keywords"
                },
                "occupations": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "copy_to": "keywords"
                },
                "location": {
                    "type": "object",
                    "properties": {
                        "translations": {
                            "type": "object",
                            "properties": {
                                "sv-SE": {
                                    "type": "text",
                                    "copy_to": "keywords",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "keywords": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword",
                            "normalizer": "lc_normalizer"
                        }
                    }
                },
            }
        }
    }
}

