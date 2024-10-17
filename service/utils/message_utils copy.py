class MessageUtils:
    def entity_not_found(entity_name, field_name, val):
        return f'No {entity_name} Found by {field_name} : {val}'
    
    def entity_not_found_two(entity_name, field_name, val, second_field_name, second_val):
        return f'No {entity_name} Found by {field_name} : {val}  and {second_field_name} : {second_val}'