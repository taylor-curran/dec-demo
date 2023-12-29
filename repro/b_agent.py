from prefect.infrastructure.process import Process
from prefect.deployments import Deployment
from prefect import flow

process_block = Process.load("boyd-process-block")


@flow(log_prints=True)
def w_flow():
    print("This is Taylor's flow")


if __name__ == "__main__":
    Deployment.build_from_flow(
        w_flow,
        "w-deployment",
        work_pool_name="agent-pool",
        infrastructure=process_block,
        apply=True,
    )
