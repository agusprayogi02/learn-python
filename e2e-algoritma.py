class server:
    base = 5
    mod = 23
    pub = 0
    key = 0

    def cari_env(self, kode: int):
        self.pub = (self.base**kode) % self.mod
        return self.pub

    def cari_key(self, kode: int, env: int):
        self.key = (env**kode) % self.mod
        return self.pub


kode = server()
ayas = kode.cari_env(6288801615824)
miko = kode.cari_env(6287857108779)
print(miko)
print(ayas)
miko = kode.cari_key(ayas, 23)
ayas = kode.cari_key(miko, 62)

print(miko)
print(ayas)
