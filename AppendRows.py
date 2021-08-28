def AppendRows(ws, name, table):
    print(name)
    try:
        bdays = table.find_all('span', {'class': 'bday'})

        if len(bdays) > 1:
            first = len(ws['A'])+1
            for bday in bdays:
                ws.append([name, bday.text])
                print(bday.text)
            last = len(ws['A'])
            ws.merge_cells('A'+str(first)+':'+'A'+str(last))
        else:
            ws.append([name, bdays[0].text])
            print(bdays[0].text)
    except Exception:
        ws.append([name, 'неизвестно'])
        print('неизвестно')
    return ws