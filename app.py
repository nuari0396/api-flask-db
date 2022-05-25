from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///db_tekkom_0396.db')


table = db['tbl_news_0396']


def fetch_db(news_id):
    return table.find_one(news_id=news_id)


def fetch_db_all():
    tbl_news_0396 = []
    for news in table:
        tbl_news_0396.append(news)
    return tbl_news_0396


@app.route('/api/db_berita', methods=['GET'])
def db_populate():
    table.insert({
        "news_id": "1",
        "judul": "pencarian harun masiku tidak bisa disampaikan ke publik",
        "isi": "Pihak Komisi Pemberantasan Korupsi (KPK) menyatakan bahwa proses penyidikan, termasuk pengejaran seseorang yang masuk dalam daftar pencarian orang (DPO) tidak bisa disampaikan kepada publik secara detail."
    })

    table.insert({
        "news_id": "2",
        "judul": "Apa yang Dicari, Jenderal Andika?",
        "isi": "TAHUN politik memaksa kita melihat peristiwa “biasa” dari sudut politik, termasuk dalam safari Panglima TNI Jenderal TNI Andika Perkasa. Terlebih, banyak mantan panglima TNI yang kemudian nyemplung ke dunia politik. Agenda apa yang dibawa Jenderal Andika ketika mengunjungi ormas-ormas Islam menjadi menarik untuk dikaji dari sisi politik."
    })

    table.insert({
        "news_id": "3",
        "judul": "THE KING HEALTH IS FAILING",
        "isi": "Back in the mid-1700s, during the height of the Jacobite rebellion in Great Britain, seditious printers printed fake news, even going so far as to report that King George II was ill, in an attempt to destabilize the establishment. Such fake news was picked up by more reputable printers and republished, making it difficult to tell fact from fiction. Responding to complaints about the practice, Attorney General Dudley Ryder wrote in a letter:"
    })

    table.insert({
        "news_id": "4",
        "judul": "REPORTS OF PEACE WITH FRANCE SEND STOCKS SOARING IN LONDON",
        "isi": "In May 1803, as Britain was preparing to end the Treaty of Amiens and declare war on France, a letter was hand delivered to Sir Charles Price, the Lord Mayor of London at the Mansion-house. Allegedly written by Lord Hawkesbury, and sealed with his personal seal, the letter claimed that the dispute with France was amicably settled. The Mayor at once took the letter to the Stock Exchange to share the joyous news."
    })

    table.insert({
        "news_id": "5",
        "judul": "LIFE ON THE MOON",
        "isi": "The article reported that Herschel had made these discoveries using new “hydro-oxygen magnifiers” and went on to describe in believable scientific detail, how the discovery was made. Bizarre life forms, inhabitants of the moon, were described, painting a fantastical picture."
    })

    table.insert({
        "news_id": "6",
        "judul": "FAKE REPORT OF OUTRAGE ON FRENCH RAILWAY",
        "isi": "Madame Marquet, the wife of an Algerian apothecary, claimed in December 1890 that she had been set upon and robbed while riding in the ladies compartment on a French train. The train had departed from Monte Carlo and on reaching Toulon, she told authorities that at some point in the journey while she was sleeping, a thief had made off with 7,000 francs."
    })

    table.insert({
        "news_id": "7",
        "judul": "JACK THE RIPPER",
        "isi": "in 1888, a series of brutal slayings in the Whitechapel district of East London were widely reported. Accounts of the eleven murders, typically involving prostitutes, were described in graphic detail in the newspapers of the time. Many tried to profit from the high profile case by spreading fake news."
    })

    table.insert({
        "news_id": "8",
        "judul": "THE REPORT OF MY DEATH WAS AN EXAGGERATION",
        "isi": "When reached for comment, Mark Twain told the reporter that he did not know whether to be amused or annoyed. He assured him that he was living with his wife and children in a very nice house in Chelsea and was hardly living in poverty, nor was he ill. It was Twain’s belief that the story came about because a cousin of his, James Ross Clemens of St Louis, was ill in London two or three weeks previously, although he had since recovered."
    })

    table.insert({
        "news_id": "9",
        "judul": "THE FAKE NEWS TRAP",
        "isi": "In 1903, the Clarksburg Daily Telegram published a purposely fake news story in an effort to expose the Clarksburg Daily News who they knew were pilfering their articles. The story was about the shooting of “Mejk Swenekafew” near Columbia mines and predictably, it appeared the next day in the Daily News. The story told of how Swenekafew, a Slav living near the Columbia coal mine was shot and was in critical condition after an altercation with an acquaintance over a pet dog."
    })

    table.insert({
        "news_id": "10",
        "judul": "THAT GOT TO DO WITH THE PRICE OF EGGS",
        "isi": "TAHUN politik memaksa kita melihat peristiwa “biasa” dari sudut politik, termasuk dalam safari Panglima TNI Jenderal TNI Andika Perkasa. Terlebih, banyak mantan panglima TNI yang kemudian nyemplung ke dunia politik. Agenda apa yang dibawa Jenderal Andika ketika mengunjungi ormas-ormas Islam menjadi menarik untuk dikaji dari sisi politik."
    })

    return make_response(jsonify(fetch_db_all()),
                         200)


@app.route('/api/tbl_news_0396', methods=['GET', 'POST'])
def api_tbl_news_0396():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        news_id = content['news_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(news_id)), 201) 


@app.route('/api/tbl_news_0396/<news_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_news(news_id):
    if request.method == "GET":
        news_obj = fetch_db(news_id)
        if news_obj:
            return make_response(jsonify(news_obj), 200)
        else:
            return make_response(jsonify(news_obj), 404)
    elif request.method == "PUT": 
        content = request.json
        table.update(content, ['news_id'])

        news_obj = fetch_db(news_id)
        return make_response(jsonify(news_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=news_id)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)