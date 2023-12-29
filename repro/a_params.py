from prefect import flow

param = [
    "Construct Excess Return Tokens Stock",
    "Flow `Stock Historical Estimation`",
    "Flow `Stock Risk Historical Estimation`",
]


@flow
def list_params_bug(param: list[str] = []):
    print(param)


if __name__ == "__main__":
    list_params_bug.deploy(
        name="list_params_bug",
        tags=["a", "repro", "params"],
        work_pool_name="my-k8s-pool",
        image="docker.io/taycurran/list-params-bug:repro",
    )
