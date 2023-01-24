# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()


# import grpc._cython.cygrpc

# grpc._cython.cygrpc.init_grpc_gevent()

from src import create_app, socketio
app = create_app()


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
