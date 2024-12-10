from frappe.model.document import Document
from frappe import _

class FlightPassenger(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        date_of_birth: DF.Date
        email: DF.Data
        first_name: DF.Data
        full_name: DF.Data | None
        last_name: DF.Data | None
        name: DF.Int | None
    # end: auto-generated types
    def before_save(self):  # Correct indentation
        if self.last_name:   # Correct alignment
            self.full_name = _("{0} {1}").format(self.first_name, self.last_name)  # Proper indentation
        else:                # `else` is now aligned with `if`
            self.full_name = self.first_name  # Proper indentation
