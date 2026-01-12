"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return (record[1])


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    tpl2str = rui_record[1][0]+rui_record[1][1]
    return tpl2str in azara_record


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    coordinates = rui_record[1][0]+rui_record[1][1]
    print (coordinates)
    if (coordinates == azara_record[1]) and (len(coordinates) == 2):
        return azara_record+rui_record
    else:
        return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""
    # make an empty list called report
    for record in combined_record_group:
        # loop through every record in the provided tuple
        report += str(record[:1] + record[2:]) + "\n"
        # add to report list the entire tuple except the item at position [1], this is done by concatenating two subsets of each tuple, one containing only the first item, one containing the third onwards
        # the square brackets indexing is exclusive after the colon but inclusive before
    return report
    total_tuples = ()
    new_combined_record_list = []
    for record in combined_record_group:
        lst_record = list(record)
        #print (lst_record)
        for i in range(len(lst_record)):
            #print (i)
            if (i != 1):
                new_combined_record_list.append(f"({lst_record[i]})\\n")
            #print (tuple(new_combined_record_list))
        total_tuples += tuple(new_combined_record_list)    
    return total_tuples

# print (get_coordinate(('Scrimshawed Whale Tooth', '2A')))
# print (convert_coordinate("2A"))
# print (compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
#print (create_record (('Amethyst  Octopus', '1F'), ('Seaside Cottages', ('1', 'C'), 'Blue')))
#print (clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))

