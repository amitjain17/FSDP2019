def information(name,email,country,subject):
    import csv
    with open('contact.csv', mode='a') as contact_file:
        contact_writer = csv.writer(contact_file, delimiter=',')
        
        contact_writer.writerow([name,email,country,subject])


        