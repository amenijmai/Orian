from config import Config

class BaseCRMClient:
    def log_interaction(self, client_email, note):
        raise NotImplementedError


class MockCRMClient(BaseCRMClient):
    def log_interaction(self, client_email, note):
        print(f"[MockCRM] Logged interaction for {client_email}: {note}")
        return True


def create_crm_client():
    if Config.CRM_PROVIDER == 'mock':
        return MockCRMClient()
    raise NotImplementedError('Only mock provider implemented')
