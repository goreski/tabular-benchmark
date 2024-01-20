
config_random  = {
}

#Defaults for TabR-S
config_default = {
    "use_gpu": {
        "value": True
    },
    "model_type": {
        "value": "david"
    },
    "model__device": {
        "value": "cuda:0" #FIXME
    },
    "transformed_target": {
        "value": False,
    },
    "transform__0__method_name": {
        "value": "gaussienize"
    },
    "transform__0__type": {
        "value": "quantile",
    },
    "transform__0__apply_on": {
        "value": "numerical",
    },
}

config_regression = {#**skorch_config,
                         **config_random ,
                                **{
                                    "model_name": {
                                        "value": "mlp_david_regressor"
                                    },
                                }}

config_regression_default = {#**skorch_config_default,
                                 **config_default,
                                **{
                                    "model_name": {
                                        "value": "mlp_david_regressor"
                                    },
                                }}

config_classif = {#**skorch_config,
                      **config_random ,
                             **{
                                 "model_name": {
                                     "value": "mlp_david"
                                 },
                             }}

config_classif_default = {#**skorch_config_default,
                              **config_default,
                             **{
                                 "model_name": {
                                     "value": "mlp_david"
                                 },
                             }}