from ldap3 import Server, Connection, ALL, NTLM

class LoginAD:
    def __init__(self, username, password):
        self.user_info = None
        self.username = username
        self.password = password
        self.host = '172.28.141.130'
        self.port = 389
        self.domain = 'SKYMOBILE_MAIN\\{}'
        self.search_filter = '(&(objectClass=user)(sAMAccountName={}))'
        self.base = 'dc=bee,dc=skymobile,dc=local'

        ldap_host = 'ldap://{}'.format(self.host)
        ldap_user = self.domain.format(self.username)

        self.server = Server(host=ldap_host, port=self.port, get_info=ALL)
        self.conn = Connection(self.server, user=ldap_user, password=self.password, authentication=NTLM)

        self.connect()
        self.get_user_info()
        self.disconnect()

    def connect(self):
        self.conn.start_tls()
        self.conn.bind()

    def disconnect(self):
        self.conn.unbind()

    def get_user_info(self):
        s_filter = self.search_filter.format(self.username)
        # 'givenName', 'sn', 'cn', 'mail', 'company', 'department', 'name', 'title', 'displayName', 'memberOf'
        x = self.conn.search(self.base, s_filter, attributes=['mail', 'displayName'])
        if x:
            self.user_info = self.conn.response[0]['attributes']

    def get(self, key):
        if self.user_info:
            return self.user_info[key]

    # returning tuple of first name and last_name
    def get_full_name(self):
        full_name = self.get('displayName')
        if full_name:
            full_name = full_name.split(' ')
            return full_name[0], full_name[1]
