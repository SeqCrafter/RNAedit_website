import reflex as rx

config = rx.Config(
    app_name="MAIRE",
    show_built_with_reflex=False,
    state_auto_setters=True,
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.sitemap.SitemapPlugin()],
)
