# Copyright 2023 DreamWorks Animation LLC and Intel Corporation
# SPDX-License-Identifier: Apache-2.0


function(ArrasCore_cxx_compile_definitions target)
    target_compile_definitions(${target}
        PRIVATE
            $<$<CONFIG:DEBUG>:
                DEBUG                               # Enables extra validation/debugging code

                # Definitions for printing debug info
                TSLOG_LEVEL=TSLOG_MSG_DEBUG
                TSLOG_SHOW_PID
                TSLOG_SHOW_TID
                TSLOG_SHOW_TIME
            >
            $<$<CONFIG:RELWITHDEBINFO>:
                BOOST_DISABLE_ASSERTS               # Disable BOOST_ASSERT macro
            >
            $<$<CONFIG:RELEASE>:
                BOOST_DISABLE_ASSERTS               # Disable BOOST_ASSERT macro
            >

        PUBLIC
            __AVX__
            _GLIBCXX_USE_CXX11_ABI=0                # https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html
            GL_GLEXT_PROTOTYPES=1                   # This define makes function symbols to be available as extern declarations.
            TBB_SUPPRESS_DEPRECATED_MESSAGES        # Suppress 'deprecated' messages from TBB
    )
endfunction()
