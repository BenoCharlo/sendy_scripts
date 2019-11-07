import xgboost as xgb


class XGB_Model:
    def __init__(self):
        return self

    def prepare_train(data, target):
        dtrain = xgb.DMatrix(data.drop("Order No", axis=1), label=target)
        return dtrain

    def prepare_test(data):
        dtest = xgb.DMatrix(data.drop("Order No"), axis=1)
        return dtest

    def train_xgb(data, params, num_boost_round):
        bst = xgb.train(params, dtrain, num_boost_round)
        return bst

    def train_xgb_cv(data, params, nfold, num_boost_round):

        cv_rmse_xgb = xgb.cv(
            params,
            dtrain,
            num_boost_round=num_boost_round,
            nfold=nfold,
            stratified=False,
            folds=None,
            metrics="rmse",
            seed=43,
        )
        return cv_rmse_xgb

    def predict_xgb(bst, data):
        return bst.predict(data)
