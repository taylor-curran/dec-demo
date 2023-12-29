import os
from prefect import flow, task
from prefect.blocks.system import String
from prefect.client import get_client
import prefect.runtime
import time
from functools import partial


async def delete_cloud_run_job(flow, flow_run, state, **kwargs):
    """Flow run state change hook that deletes a Cloud Run Job if
    the flow run crashes."""

    print(flow, flow_run, state)
    print("💥", kwargs)


@task
def sleeping_task():
    time.sleep(100)


@flow(
    on_cancellation=[partial(delete_cloud_run_job, **{"server_name": "default_server"})]
)
def cancel_flow():
    """Save the flow run name (i.e. Cloud Run job name) as a
    String block. It then executes a task that ends up crashing."""
    server_name = f"server-{prefect.runtime.flow_run.name}"
    sleeping_task()


if __name__ == "__main__":
    cancel_flow.deploy(
        name="cancel-meee",
        tags=["a", "repro"],
        work_pool_name="my-k8s-pool",
        image="docker.io/taycurran/cancel-me:repro",
        build=True,
    )
