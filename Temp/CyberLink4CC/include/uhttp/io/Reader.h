/******************************************************************
*
* uHTTP for C++
*
* Copyright (C) Satoshi Konno 2002-2013
*
* This is licensed under BSD-style license, see file COPYING.
*
******************************************************************/

#ifndef _CIO_READER_H_
#define _CIO_READER_H_

#include <uhttp/UHttpDef.h>

namespace uHTTP {
class Reader {
 public:
  Reader() {
  }

  virtual ~Reader() {
  }

  virtual ssize_t read(std::string &b, size_t len) = 0;

  virtual long skip(long n) = 0;

  virtual void unread(std::string &b, size_t off, size_t len) = 0;

  void unread(std::string &b, size_t len) {
     unread(b, 0, len);  
  }

  void unread(char c) {
    std::string b;
    b.append(&c, 0, 1);
    unread(b, 0, 1);  
  }
  
  virtual void close() = 0;

};

}

#endif

