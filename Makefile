INSTALL=install
PREFIX=/usr
#MANDIR?=/local/man/man1

TARGET := keycount

CFLAGS += -Wall
CFLAGS += `pkg-config --cflags xtst x11`
CFLAGS += `pkg-config --cflags glib-2.0`
CFLAGS += -g
LDFLAGS += `pkg-config --libs xtst x11`
LDFLAGS += `pkg-config --libs glib-2.0`
LDFLAGS += -pthread

$(TARGET): keycount.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

install:
	$(INSTALL) -Dm 755 $(TARGET) $(DESTDIR)$(PREFIX)/bin/$(TARGET)

clean:
	rm $(TARGET)

.PHONY: clean
