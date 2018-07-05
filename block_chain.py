import hashlib as hasher
import datetime

# 난이도
bits = 5

# 블록 클래스
class Block:
    def __init__(self, index, time, bits, data, previous_hash):
        self.index = index
        self.time = time
        self.bits = bits
        self.data = data
        self.previous_hash = previous_hash
        self.hash = ""
        self.nonce = 0

    def get_block_hash(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.time) + str(self.bits) + str(self.data) + str(self.previous_hash) + str(self.nonce)).encode("utf-8"))
        return sha.hexdigest()

    def mine(self):
        nonce = 0
        while not self.valid_nonce(nonce):
            nonce += 1
        print("새 블록 생성 됨: {}".format(self.hash))

    def valid_nonce(self, nonce):
        self.nonce = nonce
        self.hash = self.get_block_hash()
        i = 1
        for c in self.hash:
            if (c is not "0"):
                return False

            if (i is self.bits):
                return True
            i += 1

# Genesis 블록 생성 함수 (첫 블록)
def create_genesis_block():
    # 첫 블록은 별다른 데이터를 가지지 않는다.
    return Block(0, datetime.datetime.now(), bits, "Genesis Block", "0")

# 새 블록 생성
def next_block(prev_block, data):
    index = prev_block.index + 1
    time = datetime.datetime.now()
    previous_hash = prev_block.hash
    block = Block(index, time, bits, data, previous_hash)
    block.mine()
    return block

# 블록을 저장할 체인
block_chain = [create_genesis_block()]

# 블록 생성 + 작업증명(POW)
block_chain.append(next_block(block_chain[len(block_chain)-1], "안녕하세요"))
block_chain.append(next_block(block_chain[len(block_chain)-1], "테스트"))
block_chain.append(next_block(block_chain[len(block_chain)-1], "삘릴릴릴리 !!!"))

# 블록체인의 블록 정보 출력
for block in block_chain:
    print("블록해시: {}\n시간: {}\nNonce: {}\n블록 데이터: {}\n\n".format(block.hash, block.time, block.nonce, block.data))