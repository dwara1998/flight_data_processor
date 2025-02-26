import unittest
from flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.processor = FlightDataProcessor()
        self.sample_flights = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
        ]
        for flight in self.sample_flights:
            self.processor.add_flight(flight)

    def test_add_flight(self):
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-03-01 08:00", "arrival_time": "2025-03-01 12:30", "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 3)

    def test_add_duplicate_flight(self):
        self.processor.add_flight(self.sample_flights[0])
        self.assertEqual(len(self.processor.flights), 2)

    def test_remove_flight(self):
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 1)
        self.assertFalse(any(flight['flight_number'] == "AZ001" for flight in self.processor.flights))

    def test_flights_by_status(self):
        delayed_flights = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
        self.assertEqual(delayed_flights[0]['flight_number'], "AZ002")

    def test_get_longest_flight(self):
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight['flight_number'], "AZ001")

    def test_update_flight_status(self):
        self.processor.update_flight_status("AZ002", "ON_TIME")
        self.assertEqual(self.processor.flights_by_status("ON_TIME")[1]['flight_number'], "AZ002")

if __name__ == "__main__":
    unittest.main()
