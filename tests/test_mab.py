from mab.mab import MAB
import pytest
import pickle, codecs


@pytest.fixture
def model():
    return MAB([10, 20], [0.1, 0.5], version_ids=["version1", "version2"])


def test_type_check(model):
    assert isinstance(model, MAB)


def test_lenghts_check(model):
    assert len(model.counts) == len(model.values)


def test_narms_check(model):
    assert model.n_arms == len(model.values)


def test_reset_check(model):
    model.reset()
    assert sum(model.counts) == 30
    assert sum(model.values) == 0.6


def test_versions(model):
    assert len(model.version_ids) == 2
    assert type(model.version_ids) == list
    assert model.version_ids == ["version1", "version2"]


def test_pickle(model):
    p = model.pickle()
    unpickled_model = pickle.loads(codecs.decode(p.encode(), "base64"))
    assert type(p) == str
    assert unpickled_model == model


def test_add_arm_active_true(model):
    n_arms = model.n_arms
    model.add_arm(is_active=True)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms + 1
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_add_arm_active_false(model):
    n_arms = model.n_arms
    model.add_arm(is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_add_arm_version_active_true(model):
    n_arms = model.n_arms
    model.add_version(version_id="version3", is_active=True)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms + 1
    assert model.version_id_index("version3") in model.active_arms
    assert "version3" in model.version_ids
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_add_arm_version_active_false(model):
    n_arms = model.n_arms
    model.add_version(version_id="version3", is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert model.version_id_index("version3") not in model.active_arms
    assert "version3" in model.version_ids
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_add_arm_active_false(model):
    n_arms = model.n_arms
    model.add_arm(is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_activate_arm(model):
    # add inactive arm to the model
    n_arms = model.n_arms
    model.add_arm(is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1
    # tests for activate functions
    model.activate_arm(2)
    assert len(model.active_arms) == n_arms + 1
    assert 2 in model.active_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_activate_version(model):
    n_arms = model.n_arms
    model.add_version(version_id="version3", is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert model.version_id_index("version3") not in model.active_arms
    assert "version3" in model.version_ids
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1
    # tests for activate version
    model.activate_version("version3")
    assert model.version_id_index("version3") in model.active_arms
    assert len(model.active_arms) == n_arms + 1
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_deactivate_arm(model):
    # add active arm
    n_arms = model.n_arms
    model.add_version(version_id="version3", is_active=False)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms
    assert model.version_id_index("version3") not in model.active_arms
    assert "version3" in model.version_ids
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1

    model.deactivate_arm(2)
    assert len(model.active_arms) == n_arms
    assert 2 not in model.active_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_deactivate_version(model):
    n_arms = model.n_arms
    model.add_version(version_id="version3", is_active=True)
    assert model.n_arms == n_arms + 1
    assert len(model.active_arms) == n_arms + 1
    assert model.version_id_index("version3") in model.active_arms
    assert "version3" in model.version_ids
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1

    model.deactivate_version("version3")
    assert len(model.active_arms) == n_arms
    assert 2 not in model.active_arms
    assert len(model.counts) == n_arms + 1
    assert len(model.values) == n_arms + 1
    assert len(model.version_ids) == n_arms + 1


def test_sync_settings(model):
    settings = {"active_versions": ["version1", "version3", "version4"]}
    model.sync_settings(settings)

    assert 1 not in model.active_arms
    assert 3 == len(model.active_arms)
    assert "version2" not in model.active_versions
