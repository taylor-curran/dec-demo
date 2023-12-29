from prefect import flow


@flow(log_prints=True)
def my_hello_flow():
    print("Hello, world!")


if __name__ == "__main__":
    my_hello_flow.deploy(
        name="event-d",
        tags=["hum", "repro"],
        work_pool_name="my-k8s-pool",
        image="docker.io/taycurran/event-3:repro",
        build=False,
        push=False,
        triggers=[
            {
                "match_related": {
                    "prefect.resource.id": "prefect.flow.7f663493-3291-4b21-bd7b-8a0f50718ac3"
                },
                "expect": {"my-event.*"},
            },
            {
                "match_related": {
                    "prefect.resource.id": "prefect.flow.7f663493-3291-4b21-bd7b-8a0f50718ac3"
                },
                "expect": {"my-different-event.*"},
            }

        ],
    )
