# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    dict ={}
    if len(emails) == 0:
        for x in contacts:
            dict[x] = ""
    else:
        for i in range(0,len(emails)):
            dict[list(contacts)[i]] = emails[i]
    return dict
# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    dict = {}
    if len(contact_info) == 0 or not any(contact_info):
        for x in contacts:
            dict[x] = ""

    else:
        for i in range(0, len(contact_info)):
            contact = {}
            contact["email"] = contact_info[i][0]
            contact["phone"] = contact_info[i][1]

            dict[list(contacts)[i]] = contact
    return dict


# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE
    name = []
    email = []
    phone = []
    if contacts:
        for x in contacts:
            name.append(x)
            get_info = contacts[x]
            email.append(get_info["email"])
            phone.append(get_info["phone"])

    return [email, phone, name]

