import reflex as rx
from ..template import template


class BrowseState(rx.State):
    pass


@rx.page(
    route="/jbrowse_view",
    title="editing browse",
)
@template
def jbrowse_view() -> rx.Component:
    return rx.flex(
        rx.heading("Browse all RNA editing sites in JBrowse2:"),
        rx.el.iframe(
            src="https://seqcrafter.github.io/jbrowse-nextjs/",
            width="100%",
            height="1161px",
        ),
        direction="column",
        width="95%",
        justify="center",
        class_name="p-5 mt-20 mx-auto",
    )
