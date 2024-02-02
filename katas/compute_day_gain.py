def ComputeDayGains(nbSeats, payingGuests, guestMovements):
    seats_available = nbSeats
    guest_payments = {}
    gains = 0
    
    for movement in guestMovements:
        guest_id = movement[0]
        
        if movement[1] == 'A':  # Arrival of a guest
            if seats_available > 0 and guest_id < len(payingGuests):
                if guest_id not in guest_payments:
                    guest_payments[guest_id] = payingGuests[guest_id]
                    gains += guest_payments[guest_id]
                seats_available -= 1
        else:  # Departure of a guest
            if guest_id in guest_payments:
                seats_available += 1
                del guest_payments[guest_id]
    
    return gains

if __name__=='__main__':
    # Example inputs
    nbSeats = 5
    payingGuests = [10, 20, 15, 5, 30]
    guestMovements = [(1, 'A'), (2, 'A'), (3, 'A'), (1, 'D'), (4, 'A'),
                      (2, 'D'),
                      (3, 'D'), (5, 'A'), (5, 'D'), (4, 'D')]
    
    result = ComputeDayGains(nbSeats, payingGuests, guestMovements)
    print("Total gains for the day:", result)
