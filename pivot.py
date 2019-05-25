import pandas as pd

class Pivot():
    def __init__(self, dataframe, index, columns, values):
        self._dataframe = dataframe
        self._index = index
        self._columns = columns
        self._values = values
    
    def _pivot_dataframe(self):
        pivot_df = pd.pivot_table(
            data=self._dataframe,
            values=self._values,
            index=self._index,
            columns=self._columns,
            aggfunc='first'
        )
        pivot_df.reset_index(inplace=True)
        return pivot_df
    
    def _remove_dataframe_duplicates(self):
        drop_columns = self._columns + self._values
        self._dataframe.drop(drop_columns, inplace=True, axis=1)
        self._dataframe.drop_duplicates(inplace=True)
    
    def get_pivot_dataframe(self):
        df_pivot = self._pivot_dataframe()
        self._remove_dataframe_duplicates()
        
        final_df = pd.merge(
            left=self._dataframe,
            right=df_pivot,
            on=self._index
        )
        
        return final_df
    