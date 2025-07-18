import json
import os
import tempfile

import pytest
import tensorflow as tf

from doctr import models
from doctr.models.factory import _save_model_and_config_for_hf_hub, from_hub, push_to_hf_hub


def test_push_to_hf_hub():
    model = models.classification.resnet18(pretrained=False)
    with pytest.raises(ValueError):
        # run_config and/or arch must be specified
        push_to_hf_hub(model, model_name="test", task="classification")
    with pytest.raises(ValueError):
        # task must be one of classification, detection, recognition, obj_detection
        push_to_hf_hub(model, model_name="test", task="invalid_task", arch="mobilenet_v3_small")
    with pytest.raises(ValueError):
        # arch not in available architectures for task
        push_to_hf_hub(model, model_name="test", task="detection", arch="crnn_mobilenet_v3_large")


@pytest.mark.parametrize(
    "arch_name, task_name, dummy_model_id",
    [
        ["vgg16_bn_r", "classification", "Felix92/doctr-dummy-tf-vgg16-bn-r-v2"],
        ["resnet18", "classification", "Felix92/doctr-dummy-tf-resnet18-v2"],
        ["resnet31", "classification", "Felix92/doctr-dummy-tf-resnet31-v2"],
        ["resnet34", "classification", "Felix92/doctr-dummy-tf-resnet34-v2"],
        ["resnet34_wide", "classification", "Felix92/doctr-dummy-tf-resnet34-wide-v2"],
        ["resnet50", "classification", "Felix92/doctr-dummy-tf-resnet50-v2"],
        ["magc_resnet31", "classification", "Felix92/doctr-dummy-tf-magc-resnet31-v2"],
        ["mobilenet_v3_large", "classification", "Felix92/doctr-dummy-tf-mobilenet-v3-large-v2"],
        ["vit_b", "classification", "Felix92/doctr-dummy-tf-vit-b-v2"],
        ["textnet_tiny", "classification", "Felix92/doctr-dummy-tf-textnet-tiny-v2"],
        ["db_resnet50", "detection", "Felix92/doctr-dummy-tf-db-resnet50-v2"],
        ["db_mobilenet_v3_large", "detection", "Felix92/doctr-dummy-tf-db-mobilenet-v3-large-v2"],
        ["linknet_resnet18", "detection", "Felix92/doctr-dummy-tf-linknet-resnet18-v2"],
        ["linknet_resnet50", "detection", "Felix92/doctr-dummy-tf-linknet-resnet50-v2"],
        ["linknet_resnet34", "detection", "Felix92/doctr-dummy-tf-linknet-resnet34-v2"],
        ["crnn_vgg16_bn", "recognition", "Felix92/doctr-dummy-tf-crnn-vgg16-bn-v2"],
        ["crnn_mobilenet_v3_large", "recognition", "Felix92/doctr-dummy-tf-crnn-mobilenet-v3-large-v2"],
        ["sar_resnet31", "recognition", "Felix92/doctr-dummy-tf-sar-resnet31-v2"],
        ["master", "recognition", "Felix92/doctr-dummy-tf-master-v2"],
        ["vitstr_small", "recognition", "Felix92/doctr-dummy-tf-vitstr-small-v2"],
        ["parseq", "recognition", "Felix92/doctr-dummy-tf-parseq-v2"],
    ],
)
def test_models_for_hub(arch_name, task_name, dummy_model_id, tmpdir):
    with tempfile.TemporaryDirectory() as tmp_dir:
        tf.keras.backend.clear_session()
        model = models.__dict__[task_name].__dict__[arch_name](pretrained=True)

        _save_model_and_config_for_hf_hub(model, arch=arch_name, task=task_name, save_dir=tmp_dir)

        assert hasattr(model, "cfg")
        assert len(os.listdir(tmp_dir)) == 2
        assert os.path.exists(tmp_dir + "/tf_model.weights.h5")
        assert os.path.exists(tmp_dir + "/config.json")
        tmp_config = json.load(open(tmp_dir + "/config.json"))
        assert arch_name == tmp_config["arch"]
        assert task_name == tmp_config["task"]
        assert all(key in model.cfg.keys() for key in tmp_config.keys())

        # test from hub
        tf.keras.backend.clear_session()
        hub_model = from_hub(repo_id=dummy_model_id)
        assert isinstance(hub_model, type(model))
