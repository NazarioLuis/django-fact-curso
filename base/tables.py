import django_tables2 as tables


class BaseTable(tables.Table):
    def get_options(links):
        return tables.TemplateColumn(
            template_name='base/list_options.html', verbose_name="Opciones",
            extra_context=links
        )

    class Meta:
        attrs = {"class": "table table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        abstract = True
