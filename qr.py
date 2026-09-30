#!/usr/bin/env python3
"""QR generator sederhana (butuh: pip install qrcode[pil])."""
import qrcode, sys
def main():
      data = sys.argv[1] if len(sys.argv) > 1 else input("text/url: ")
      img = qrcode.make(data)
      out = input("nama file [qr.png]: ") or "qr.png"
      img.save(out); print("saved:", out)
  if __name__ == "__main__": main()
    
