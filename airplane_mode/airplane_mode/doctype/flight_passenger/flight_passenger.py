from frappe.model.document import Document
from frappe import _

class FlightPassenger(Document):
    def before_save(self):  # Correct indentation
        if self.last_name:   # Correct alignment
            self.full_name = _("{0} {1}").format(self.first_name, self.last_name)  # Proper indentation
        else:                # `else` is now aligned with `if`
            self.full_name = self.first_name  # Proper indentation
