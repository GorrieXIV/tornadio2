``tornadio3.polling``
=====================

.. automodule:: tornadio3.polling

	.. autoclass:: TornadioPollingHandlerBase

	Request
	^^^^^^^

	.. automethod:: TornadioPollingHandlerBase.get
	.. automethod:: TornadioPollingHandlerBase.post

	Callbacks
	^^^^^^^^^

	.. automethod:: TornadioPollingHandlerBase.session_closed
	.. automethod:: TornadioPollingHandlerBase.on_connection_close

	Output
	^^^^^^

	.. automethod:: TornadioPollingHandlerBase.send_messages


	Sessions
	^^^^^^^^

	.. automethod:: TornadioPollingHandlerBase._get_session
	.. automethod:: TornadioPollingHandlerBase._detach


	.. autoclass:: TornadioXHRPollingHandler

	.. autoclass:: TornadioHtmlFileHandler

	.. autoclass:: TornadioJSONPHandler
