import pytest
from unittest.mock import AsyncMock, MagicMock, patch

# Import the classes to be tested
from your_module import (
    BusinessAddressAccessRouters,
    BusinessHandler,
    BusinessAddressApplicationDB,
    HTTPException,
)


@pytest.fixture
def mocked_session():
    # Mock the database session
    return MagicMock()


def test_register_business_address_handler():
    # Mock the payload
    class MockPayload:
        def __init__(self):
            self.street = "Test Street"
            self.number = "123"
            self.exterior = "A"
            self.interior = "B"
            self.postal_code = "12345"
            self.colony = "Test Colony"
            self.country = "Test Country"
            self.fiscal_address = "Test Fiscal Address"

    payload = MockPayload()

    # Mock the BusinessAddressApplicationDB and SQLPostgresConnectionRepository
    app_mock = MagicMock()
    app_mock.register_business_address_application.return_value = payload

    conn_mock = MagicMock()
    conn_mock.insert_payload_repository.return_value = payload

    with patch("your_module.BusinessAddressApplicationDB", return_value=app_mock):
        with patch("your_module.SQLPostgresConnectionRepository", return_value=conn_mock):
            # Instantiate the BusinessHandler
            handler = BusinessHandler()

            # Call the register_business_address_handler method
            result = handler.register_business_address_handler(payload)

            # Assert the result
            assert result == payload
            app_mock.register_business_address_application.assert_called_once_with(payload)
            conn_mock.insert_payload_repository.assert_called_once_with(payload)


@pytest.mark.asyncio
async def test_register_business_address_handler_with_error(mocked_session):
    # Mock the payload with missing data
    class MockPayload:
        def __init__(self):
            self.street = "Test Street"
            # Missing other required fields

    payload = MockPayload()

    # Mock the BusinessAddressApplicationDB and SQLPostgresConnectionRepository
    app_mock = MagicMock()
    app_mock.register_business_address_application.side_effect = HTTPException(status_code=400, detail="Invalid payload")

    with patch("your_module.BusinessAddressApplicationDB", return_value=app_mock):
        with patch("your_module.SQLPostgresConnectionRepository", return_value=mocked_session):
            # Instantiate the BusinessHandler
            handler = BusinessHandler()

            # Call the register_business_address_handler method and expect an HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await handler.register_business_address_handler(payload)

            # Assert the raised HTTPException
            assert exc_info.value.status_code == 400
            assert exc_info.value.detail == "Invalid payload"
            app_mock.register_business_address_application.assert_called_once_with(payload)
            mocked_session.insert_payload_repository.assert_not_called()


if __name__ == "__main__":
    pytest.main()
