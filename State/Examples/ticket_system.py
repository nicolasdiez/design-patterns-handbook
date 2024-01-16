from abc import ABC, abstractmethod

# Abstract base class TicketState
class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass

# Concrete state classes (NewState, AssignedState, ResolvedState, and ClosedState)

class NewState(TicketState):

    def assign(self, ticket: 'Ticket'):
        # Behavior for assigning a new ticket
        ticket.state = AssignedState()
        print(f'Ticket {ticket} has been assigned')

    def resolve(self, ticket: 'Ticket'):
        # Behavior for resolving a new ticket
        print(f'Ticket {ticket} must be assigned first')

    def close(self, ticket: 'Ticket'):
        # Behavior for closing a new ticket
        ticket.state = ClosedState()
        print(f'Ticket {ticket} has been closed')


class AssignedState(TicketState):
    
    def assign(self, ticket: 'Ticket'):
        # Behavior for assigning a new ticket
        print(f'Ticket {ticket} is already assigned')

    def resolve(self, ticket: 'Ticket'):
        # Behavior for resolving a new ticket
        ticket.state = ResolvedState()
        print(f'Ticket {ticket} has been resolved')

    def close(self, ticket: 'Ticket'):
        # Behavior for closing a new ticket
        ticket.state = ClosedState()
        print(f'Ticket {ticket} has been closed')


class ResolvedState(TicketState):
    
    def assign(self, ticket: 'Ticket'):
        # Behavior for assigning a new ticket
        print(f'Ticket {ticket} has been already resolved, it can not be assigned again')

    def resolve(self, ticket: 'Ticket'):
        # Behavior for resolving a new ticket
        print(f'Ticket {ticket} is already resolved')

    def close(self, ticket: 'Ticket'):
        # Behavior for closing a new ticket
        ticket.state = ClosedState()
        print(f'Ticket {ticket} has been closed')


class ClosedState(TicketState):
    
    def assign(self, ticket: 'Ticket'):
        # Behavior for assigning a new ticket
        print(f'Ticket {ticket} is already closed, it can not be assigned again')

    def resolve(self, ticket: 'Ticket'):
        # Behavior for resolving a new ticket
        print(f'Ticket {ticket} is already resolved')

    def close(self, ticket: 'Ticket'):
        # Behavior for closing a new ticket
        print(f'Ticket {ticket} is already closed')


# Context (Ticket class)
class Ticket:

    def __init__(self):
        # Initialize the ticket's state attribute with an instance of the NewState class
        self.state: TicketState = NewState()

    def assign(self):
        # Delegate the assign method call to the current state object
        self.state.assign(self)

    def resolve(self):
        # Delegate the resolve method call to the current state object
        self.state.resolve(self)

    def close(self):
        # Delegate the close method call to the current state object
        self.state.close(self)


# Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()

if __name__ == "__main__":
    main()
