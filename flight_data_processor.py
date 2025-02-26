from typing import List, Dict
import datetime

class FlightDataProcessor:
    def __init__(self) -> None:
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        if not any(flight['flight_number'] == data['flight_number'] for flight in self.flights):
            departure = datetime.datetime.strptime(data["departure_time"], "%Y-%m-%d %H:%M")
            arrival = datetime.datetime.strptime(data["arrival_time"], "%Y-%m-%d %H:%M")
            data["duration_minutes"] = int((arrival - departure).total_seconds() // 60)
            self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        return [flight for flight in self.flights if flight['status'] == status]

    def get_longest_flight(self) -> Dict:
        return max(self.flights, key=lambda x: x['duration_minutes'], default={})

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status
                break
