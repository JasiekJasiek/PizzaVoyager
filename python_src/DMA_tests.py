import unittest
from unittest.mock import patch, Mock
from DMA import get_distances 

class TestGetDistances(unittest.TestCase):

    @patch('DMA.requests.get') 
    def test_valid_input(self, mock_get):
        """Test with valid input and a mocked API response."""
        mock_response = {
            "status": "OK",
            "rows": [
                {
                    "elements": [
                        {"distance": {"text": "0 km"}},
                        {"distance": {"text": "130 km"}},
                        {"distance": {"text": "340 km"}}
                    ]
                },
                {
                    "elements": [
                        {"distance": {"text": "130 km"}},
                        {"distance": {"text": "0 km"}},
                        {"distance": {"text": "320 km"}}
                    ]
                },
                {
                    "elements": [
                        {"distance": {"text": "340 km"}},
                        {"distance": {"text": "320 km"}},
                        {"distance": {"text": "0 km"}}
                    ]
                }
            ]
        }

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_response

        locations = ['Warszawa, Polska', 'Łódź, Polska', 'Gdańsk, Polska']
        API_KEY = "dummy_key"

        expected_distance_matrix = [
            [0, 130000, 340000],
            [130000, 0, 320000],
            [340000, 320000, 0]
        ]

        result = get_distances(locations, API_KEY)
        self.assertEqual(result, expected_distance_matrix)

    @patch('DMA.requests.get')
    def test_empty_input(self, mock_get):
        """Test with an empty list of locations."""
        locations = []
        API_KEY = "dummy_key"

        result = get_distances(locations, API_KEY)
        self.assertEqual(result, []) 

    @patch('DMA.requests.get')
    def test_api_error_response(self, mock_get):
        """Test when the API returns an error response."""
        mock_response = {
            "status": "REQUEST_DENIED",
            "error_message": "The provided API key is invalid."
        }

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_response

        locations = ['Warszawa, Polska', 'Łódź, Polska']
        API_KEY = "invalid_key"

        result = get_distances(locations, API_KEY)
        self.assertEqual(result, []) 


if __name__ == '__main__':
    unittest.main()
