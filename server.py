from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpan data pengguna (username dan password) sementara
user_credentials = {
    'AllTools': '__troBosAJG0992103129%$#@__',
    'WA104%2': '__underLine9021021183$__',
    'MD52839_%$': '__DefaceAjaBang09182*#$__123'
    'InstallerSekte': '__230002Sekte*)__',
    'PyDependen': '__InstallSendiriKONT*l01322__',
    'DDoS_GSN&%#': '__anjingPegelOtakguaNgen@$13167__',
    'BACKDOOR_MAKER': '__0012830MUDAHinimah__',
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in user_credentials and user_credentials[username] == password:
        return jsonify({'message': 'Authentication successful'}), 200
    else:
        return jsonify({'message': 'Authentication failed'}), 401

if __name__ == '__main__':
    app.run(debug=True)
