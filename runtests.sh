#!/bin/bash
source venv/Scripts/activate
pytest
TEST_EXIT=$?
if pytest; then
    echo "All tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi