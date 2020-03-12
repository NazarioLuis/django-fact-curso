from base.tables import BaseTable,tables
from .models import Categoria,SubCategoria,Marca

class MarcaTable(BaseTable):
    options = BaseTable.get_options({
        "url_edit": "inv:marca_edit",
        "url_delete": "inv:marca_delete",
        "url_view": "inv:marca_view",
    })

    class Meta(BaseTable.Meta):

        model = Marca
        fields = ("descripcion", "estado", "fecha_creacion",
                  "fecha_modificacion", "options",)

class CategoriaTable(BaseTable):
    options = BaseTable.get_options({
        "url_edit": "inv:categoria_edit",
        "url_delete": "inv:categoria_delete",
        "url_view": "inv:categoria_view",
    })

    class Meta(BaseTable.Meta):

        model = Categoria
        fields = ("descripcion", "estado", "fecha_creacion",
                  "fecha_modificacion", "options",)


class SubCategoriaTable(BaseTable):
    options = BaseTable.get_options({
        "url_edit": "inv:subcategoria_edit",
        "url_delete": "inv:subcategoria_delete",
        "url_view": "inv:subcategoria_view",
    })

    class Meta(BaseTable.Meta):
        model = SubCategoria
        fields = ("categoria","descripcion","estado", "fecha_creacion","fecha_modificacion", "options",)
