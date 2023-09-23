from django.apps import apps


def get_client_model():
    return apps.get_model("client", "Client")


def get_brand_model():
    return apps.get_model("device", "Brand")


def get_device_model_model():
    return apps.get_model("device", "DeviceModel")


def get_device_model():
    return apps.get_model("device", "Device")


def get_invoice_model():
    return apps.get_model("invoice", "Invoice")


def get_invoice_item_model():
    return apps.get_model("invoice", "InvoiceItem")


def get_role_model():
    return apps.get_model("permission", "Role")


def get_role_permission_model():
    return apps.get_model("permission", "RolePermission")


def get_person_model():
    return apps.get_model("person", "Person")


def get_phone_model():
    return apps.get_model("phone", "Phone")


def get_product_model():
    return apps.get_model("product", "Product")


def get_service_model():
    return apps.get_model("repair", "Service")


def get_repair_model():
    return apps.get_model("repair", "Repair")


def get_repair_status_model():
    return apps.get_model("repair", "RepairStatus")


def get_user_model():
    return apps.get_model("user", "User")
