from prefect import flow
from prefect.events import emit_event
import time
from uuid import uuid4
import datetime


@flow
def emit_4_events():
    x = uuid4()
    emit_event(
        event="my-different-event." + f"-- {datetime.datetime.now()} --" + str(x),
        resource={"prefect.resource.id": "event-emitting-flow"},
    )

    for i in range(3):
        x = uuid4()
        emit_event(
            event="my-event." + f"-- {i} --" + str(x),
            resource={"prefect.resource.id": "event-emitting-flow"},
        )

if __name__ == "__main__":
    emit_4_events()
