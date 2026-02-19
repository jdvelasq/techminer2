from techminer2.ingest.sources.scopus import Scopus


def test_ingestion_addtech():
    result = Scopus().where_root_directory("examples/adtech/").run()
    assert result.success


def test_ingestion_big_data_analytics():
    result = Scopus().where_root_directory("examples/big-data-analytics/").run()
    assert result.success


def test_ingestion_blended_learning():
    result = Scopus().where_root_directory("examples/blended-learning/").run()
    assert result.success


def test_ingestion_business_analytics():
    result = Scopus().where_root_directory("examples/business-analytics/").run()
    assert result.success


def test_ingestion_business_intelligence():
    result = Scopus().where_root_directory("examples/business-intelligence/").run()
    assert result.success


def test_ingestion_chain_analytics():
    result = Scopus().where_root_directory("examples/chain-analytics/").run()
    assert result.success


def test_ingestion_digital_twins():
    result = Scopus().where_root_directory("examples/digital-twins/").run()
    assert result.success


def test_ingestion_govtech():
    result = Scopus().where_root_directory("examples/govtech/").run()
    assert result.success


def test_ingestion_hrtech():
    result = Scopus().where_root_directory("examples/hrtech/").run()
    assert result.success


def test_ingestion_learning_analytics():
    result = Scopus().where_root_directory("examples/learning-analytics/").run()
    assert result.success


def test_ingestion_legaltech():
    result = Scopus().where_root_directory("examples/legaltech/").run()
    assert result.success


def test_ingestion_martech():
    result = Scopus().where_root_directory("examples/martech/").run()
    assert result.success


def test_ingestion_people_analytics():
    result = Scopus().where_root_directory("examples/people-analytics/").run()
    assert result.success


def test_ingestion_proptech():
    result = Scopus().where_root_directory("examples/proptech/").run()
    assert result.success


def test_ingestion_regtech():
    result = Scopus().where_root_directory("examples/regtech/").run()
    assert result.success


def test_ingestion_retail_analytics():
    result = Scopus().where_root_directory("examples/retail-analytics/").run()
    assert result.success


def test_ingestion_tinyml():
    result = Scopus().where_root_directory("examples/tinyml/").run()
    assert result.success


def test_ingestion_wealthtech():
    result = Scopus().where_root_directory("examples/wealthtech/").run()
    assert result.success
