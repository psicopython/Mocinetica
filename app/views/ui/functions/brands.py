from typing import Any

from flask import render_template, request


class BrandUI:

    @classmethod
    def listBrands(cls, *args, **kwargs) -> Any:
        return render_template("/base.html", *args, **kwargs), 200