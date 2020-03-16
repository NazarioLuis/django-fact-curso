from base.tables import BaseTable,tables
from .models import Proveedor

class ProveedorTable(BaseTable):
    options = BaseTable.get_options({
        "url_edit": "cmp:proveedor_edit",
        "url_delete": "cmp:proveedor_delete",
        "url_view": "cmp:proveedor_view",
    })

    class Meta(BaseTable.Meta):
        model = Proveedor
        fields = ("descripcion", "estado", "fecha_creacion",
                  "fecha_modificacion", "options",)