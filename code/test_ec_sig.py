import gc, ngu  # auto-gen
for i in range(25):
  cur = ngu.ec.curve(ngu.ec.SECP256K1)
  assert cur.sign(b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b'\xf7T\x18\xc5rz\\&e\xbb\xe8\xed\x8e\x1dfg\xb2U\xf5\tA\xfdo\n_\xab\x12f\xe7$\x85A\xc2*}"%1\x16H)S^zxk\x7f0y\x1flI!\x87\xa8&\xdf\xd8\xb5\xb7\xb2,\xe7t'
  assert cur.verify(b'\x04\x9a\xc2\x035\xeb8v\x8d R\xbe\x1d\xbb\xc3\xc8\xf6\x17\x84\x07E\x8eQ\xe6\xb4\xad"\xf1\xd9\x17X\x89[\xaf\x10*`?\xa0\x9b6g\x05\xfdrwW\xa5\xab\xd6\x14A\nn?\x80*\xb8\xda\x8d\xfe\x84(\x9dd', b'\xf7T\x18\xc5rz\\&e\xbb\xe8\xed\x8e\x1dfg\xb2U\xf5\tA\xfdo\n_\xab\x12f\xe7$\x85A\xc2*}"%1\x16H)S^zxk\x7f0y\x1flI!\x87\xa8&\xdf\xd8\xb5\xb7\xb2,\xe7t', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x04\x9a\xc2\x035\xeb8v\x8d R\xbe\x1d\xbb\xc3\xc8\xf6\x17\x84\x07E\x8eQ\xe6\xb4\xad"\xf1\xd9\x17X\x89[\xaf\x10*`?\xa0\x9b6g\x05\xfdrwW\xa5\xab\xd6\x14A\nn?\x80*\xb8\xda\x8d\xfe\x84(\x9dd', b'\xf7T\x18\xc5rz\\&e\xbb\xe8\xed\x8e\x1dfg\xb2U\xf5\tA\xfdo\n_\xab\x12f\xe7$\x85A\xc2*}"%1\x16H)S^zxk\x7f0y\x1flI!\x87\xa8&\xdf\xd8\xb5\xb7\xb2,\x00\x00', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  cur = ngu.ec.curve(ngu.ec.BP256R1)
  assert cur.sign(b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b'\x00\x9b\xb8uz\xb7\xb4g\x0f\x01\xe1\xb3\xc2\xc6\x9fK\xfaKNs5Z?Q\xb7\xe0\xbav`$\x8f\x04]\xcaB\xf5\xfcM;\xe8\x96\x98\x9a`H\x96\xf57,T\x03\\\xae\xe6\xf1\xf2\xfam\xab\xa3L\xd1\xf8\x9f'
  assert cur.verify(b'\x04z\xacd\xeaJ\xb3\t\xacm\x1fW"\x12\xb4\xe3OK\x92f\xf3_f\xab\xe7vjX\rY\x1d\x98V)\x88\xc8\x92<*\x9f\xfe\x05\'\xa0mvp\x892\xe5\xd0={\x19\xed\xed\x18U\xe5\xbc\x87\xf7\xe3\xb4\xb3', b'\x00\x9b\xb8uz\xb7\xb4g\x0f\x01\xe1\xb3\xc2\xc6\x9fK\xfaKNs5Z?Q\xb7\xe0\xbav`$\x8f\x04]\xcaB\xf5\xfcM;\xe8\x96\x98\x9a`H\x96\xf57,T\x03\\\xae\xe6\xf1\xf2\xfam\xab\xa3L\xd1\xf8\x9f', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x04z\xacd\xeaJ\xb3\t\xacm\x1fW"\x12\xb4\xe3OK\x92f\xf3_f\xab\xe7vjX\rY\x1d\x98V)\x88\xc8\x92<*\x9f\xfe\x05\'\xa0mvp\x892\xe5\xd0={\x19\xed\xed\x18U\xe5\xbc\x87\xf7\xe3\xb4\xb3', b'\x00\x9b\xb8uz\xb7\xb4g\x0f\x01\xe1\xb3\xc2\xc6\x9fK\xfaKNs5Z?Q\xb7\xe0\xbav`$\x8f\x04]\xcaB\xf5\xfcM;\xe8\x96\x98\x9a`H\x96\xf57,T\x03\\\xae\xe6\xf1\xf2\xfam\xab\xa3L\xd1\x00\x00', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  cur = ngu.ec.curve(ngu.ec.NIST_P256)
  assert cur.sign(b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b"\x99\xdbu\xdfht\x7f\xdf\xf4M_O\xcb\x0f\x81\xd4|4\xb9\xc6q\xfeI\x81\t{o\xb5\xd3A\xf1=Ul\x00\xf1)tBhZN'\xd8\x18\xac\x1a\xc9r,\xa0\xac\xf3\xd3\xf9\xe9\x15\xb1\x1e\xef\x96\xa6\xba\xb8"
  assert cur.verify(b'\x04W\xe9w\xf6\xdb~3\xc3\xfez\xcf(B\xed\x98p\t\xca\xf5mE\x86\x82\xfc\xa4G\xb7\xd3\xd7b\xab4\xc5\xab7p\xbaW;\xdf\xf5A@ed\x0f\xfb[4m\xfa\x84\xde\xc4\xdbMh\xe5\xf5\x9c\xc4q\xc2\xec', b"\x99\xdbu\xdfht\x7f\xdf\xf4M_O\xcb\x0f\x81\xd4|4\xb9\xc6q\xfeI\x81\t{o\xb5\xd3A\xf1=Ul\x00\xf1)tBhZN'\xd8\x18\xac\x1a\xc9r,\xa0\xac\xf3\xd3\xf9\xe9\x15\xb1\x1e\xef\x96\xa6\xba\xb8", b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x04W\xe9w\xf6\xdb~3\xc3\xfez\xcf(B\xed\x98p\t\xca\xf5mE\x86\x82\xfc\xa4G\xb7\xd3\xd7b\xab4\xc5\xab7p\xbaW;\xdf\xf5A@ed\x0f\xfb[4m\xfa\x84\xde\xc4\xdbMh\xe5\xf5\x9c\xc4q\xc2\xec', b"\x99\xdbu\xdfht\x7f\xdf\xf4M_O\xcb\x0f\x81\xd4|4\xb9\xc6q\xfeI\x81\t{o\xb5\xd3A\xf1=Ul\x00\xf1)tBhZN'\xd8\x18\xac\x1a\xc9r,\xa0\xac\xf3\xd3\xf9\xe9\x15\xb1\x1e\xef\x96\xa6\x00\x00", b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  cur = ngu.ec.curve(ngu.ec.SECP256K1)
  assert cur.sign(b'\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b't\x1d\x0cc\xfcI\xbb4U\x98!\xfa;A*\xe1\x01\xf6\x9b\xae\xc0\x87\xaa\xc3\xc0\xcc9(&\x92\xe2\xc7*_\x92D\x9b\xc76{\x17\x82\x16\x06\x05E\xefqeBY\xa7\xeeVM\x97\x95\x92q\\\x7f\xb9?\xcf'
  assert cur.verify(b'\x046\x07KP\xb9\xc9\xd5Na;\thGB\x0bHnL\x8f\xf6\xc7\xb4\xe6{\x12\xf5b\xda%aUi\xd5\x0c\xde\xe6@I\xeb\xf6M\x89"6\xc3\xedQ9|\x8e\xd4\xc0\xb6\xc4E\xe1Wn\xf9q2\xdaR\xa3', b't\x1d\x0cc\xfcI\xbb4U\x98!\xfa;A*\xe1\x01\xf6\x9b\xae\xc0\x87\xaa\xc3\xc0\xcc9(&\x92\xe2\xc7*_\x92D\x9b\xc76{\x17\x82\x16\x06\x05E\xefqeBY\xa7\xeeVM\x97\x95\x92q\\\x7f\xb9?\xcf', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x046\x07KP\xb9\xc9\xd5Na;\thGB\x0bHnL\x8f\xf6\xc7\xb4\xe6{\x12\xf5b\xda%aUi\xd5\x0c\xde\xe6@I\xeb\xf6M\x89"6\xc3\xedQ9|\x8e\xd4\xc0\xb6\xc4E\xe1Wn\xf9q2\xdaR\xa3', b't\x1d\x0cc\xfcI\xbb4U\x98!\xfa;A*\xe1\x01\xf6\x9b\xae\xc0\x87\xaa\xc3\xc0\xcc9(&\x92\xe2\xc7*_\x92D\x9b\xc76{\x17\x82\x16\x06\x05E\xefqeBY\xa7\xeeVM\x97\x95\x92q\\\x7f\xb9\x00\x00', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  cur = ngu.ec.curve(ngu.ec.BP256R1)
  assert cur.sign(b'\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b'\x9e}A+(\x8a\x9b\xd8\x9f\x0b\xc7\x8e\x02\x93\x8aB\xf5\x82\xf0\x1e\xd5B#fik+\xa8R\xa8P\xd5jA\xb0\xfb\x82\xea\x03\x11\x91\xa9\xc5(Z\xcb\xaf\xd4\xfa\x02\x93\x82\x1b\x82!I\xe2k\xbe\xf9j\x90\xd8\xe8'
  assert cur.verify(b'\x04BjF&\x9b\xa0\x96O\xd8\x01\x98\x03q\x90\x19\x89\xd4\xde\x06\xb9-\x89q\x90;^\xeb\x03\xd0\xa6\x8a)/@u\x94\xb3\x9f\xb3\xa4\xb7\x1aa\x18\x0c\xf36/\x16F\x08W\xaa\x1e\xe8\x1eBr\xa2\xef\xb0\xba?\x18', b'\x9e}A+(\x8a\x9b\xd8\x9f\x0b\xc7\x8e\x02\x93\x8aB\xf5\x82\xf0\x1e\xd5B#fik+\xa8R\xa8P\xd5jA\xb0\xfb\x82\xea\x03\x11\x91\xa9\xc5(Z\xcb\xaf\xd4\xfa\x02\x93\x82\x1b\x82!I\xe2k\xbe\xf9j\x90\xd8\xe8', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x04BjF&\x9b\xa0\x96O\xd8\x01\x98\x03q\x90\x19\x89\xd4\xde\x06\xb9-\x89q\x90;^\xeb\x03\xd0\xa6\x8a)/@u\x94\xb3\x9f\xb3\xa4\xb7\x1aa\x18\x0c\xf36/\x16F\x08W\xaa\x1e\xe8\x1eBr\xa2\xef\xb0\xba?\x18', b'\x9e}A+(\x8a\x9b\xd8\x9f\x0b\xc7\x8e\x02\x93\x8aB\xf5\x82\xf0\x1e\xd5B#fik+\xa8R\xa8P\xd5jA\xb0\xfb\x82\xea\x03\x11\x91\xa9\xc5(Z\xcb\xaf\xd4\xfa\x02\x93\x82\x1b\x82!I\xe2k\xbe\xf9j\x90\x00\x00', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  cur = ngu.ec.curve(ngu.ec.NIST_P256)
  assert cur.sign(b'\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == b'\x86\x1b\xa9.W\x80\x9a\x97RL\xea\x1c\x1b\xf7\xc7\xed\xb7\xbeH\xfd&#\xb6^*\xd2\x93(+\xee*e}\xfb\xce\x87\x8b:o\xbai\xb4d\xeb\xd6\x90\x8c\xe2}\xec\x97\xaa0\x17y\xdeF\n{5#\x0e\x1d:'
  assert cur.verify(b'\x04\x11\x9a\xd9\r\x1c\x9c>6\x07\x7f\xfa\x19Y\xec7<\xfd\x0c\xdc\xbe\xf6`\t\x05yF\xf7V\\6\xc1\x8d\x039(\x89\xbbm\xcaK9NrU\t|^\xf4H4\xe0\x82\x9c\xbc\xd2>d-x{\xd9\x1a\xcf\xf3', b'\x86\x1b\xa9.W\x80\x9a\x97RL\xea\x1c\x1b\xf7\xc7\xed\xb7\xbeH\xfd&#\xb6^*\xd2\x93(+\xee*e}\xfb\xce\x87\x8b:o\xbai\xb4d\xeb\xd6\x90\x8c\xe2}\xec\x97\xaa0\x17y\xdeF\n{5#\x0e\x1d:', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == True
  assert cur.verify(b'\x04\x11\x9a\xd9\r\x1c\x9c>6\x07\x7f\xfa\x19Y\xec7<\xfd\x0c\xdc\xbe\xf6`\t\x05yF\xf7V\\6\xc1\x8d\x039(\x89\xbbm\xcaK9NrU\t|^\xf4H4\xe0\x82\x9c\xbc\xd2>d-x{\xd9\x1a\xcf\xf3', b'\x86\x1b\xa9.W\x80\x9a\x97RL\xea\x1c\x1b\xf7\xc7\xed\xb7\xbeH\xfd&#\xb6^*\xd2\x93(+\xee*e}\xfb\xce\x87\x8b:o\xbai\xb4d\xeb\xd6\x90\x8c\xe2}\xec\x97\xaa0\x17y\xdeF\n{5#\x0e\x00\x00', b'MSG1MSG1MSG1MSG1MSG1MSG1MSG1MSG1') == False
  del cur
  gc.collect()
print('PASS')
