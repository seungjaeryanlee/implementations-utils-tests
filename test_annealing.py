"""Test utils.get_linear_anneal_func."""
import types

import pytest

from utils import get_linear_anneal_func


class TestGetLinearAnnealFunc:
    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_type(self, start_value, end_value, start_step, end_step):
        """Test the return type of get_linear_anneal_func."""
        print(start_value)
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        assert isinstance(linear_anneal_func, types.FunctionType)

    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_func_return_type(
        self, start_value, end_value, start_step, end_step
    ):
        """Test the return type of linear_anneal_func."""
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        value = linear_anneal_func(end_step)
        assert isinstance(value, float) or isinstance(value, int)

    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_func_start_value(
        self, start_value, end_value, start_step, end_step
    ):
        """Test the start value of linear_anneal_func."""
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        value = linear_anneal_func(start_step)
        assert value == start_value

    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_func_mid_value(self, start_value, end_value, start_step, end_step):
        """Test the middle value of linear_anneal_func."""
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        value = linear_anneal_func((end_step - start_step) / 2)
        assert value == (start_value - end_value) / 2

    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_func_end_value(self, start_value, end_value, start_step, end_step):
        """Test the end value of linear_anneal_func."""
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        value = linear_anneal_func(end_step)
        assert value == end_value

    @pytest.mark.parametrize(
        "start_value, end_value, start_step, end_step", [(1, 0, 0, 100), (2, 0, 0, 10)]
    )
    def test_return_func_after_end_value(
        self, start_value, end_value, start_step, end_step
    ):
        """Test the value of linear_anneal_func after end_steps."""
        linear_anneal_func = get_linear_anneal_func(
            start_value, end_value, start_step, end_step
        )
        value = linear_anneal_func(end_step + 1)
        assert value == end_value
