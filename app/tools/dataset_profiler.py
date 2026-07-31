from app.models.dataset_profile import DatasetProfile
import pandas as pd
from app.utils.logger import get_logger

logger = get_logger(__name__)

class DatasetProfiler:

    def run(self, df:pd.DataFrame, target_column:str | None = None) -> DatasetProfile:
        """
        Analyze the dataset and return a DatasetProfile.
        """
        
        if df is None:
            raise ValueError("Input DataFrame cannot be None.")

        if df.empty:
            raise ValueError("Input DataFrame is empty.")
        if target_column is not None and target_column not in df.columns:
                raise ValueError(
                    f"Target column '{target_column}' does not exist in the dataset."
                )

        logger.info("Starting dataset profiling")

        rows = len(df)

        columns = len(df.columns)

        column_names = df.columns.tolist()
        
        numerical_columns = (
            df.select_dtypes(include="number")
            .columns
            .tolist()
        )

        categorical_columns = (
            df.select_dtypes(exclude="number")
            .columns
            .tolist()
        )
        
        missing_values = (
            df.isnull()
            .sum()
            .to_dict()
        )
        
        duplicate_rows = int(df.duplicated().sum())
        
        
        profile = DatasetProfile(
            rows=rows,
            columns=columns,
            column_names=column_names,
            numerical_columns=numerical_columns,
            categorical_columns=categorical_columns,
            missing_values=missing_values,
            duplicate_rows=duplicate_rows,
            target_column=target_column,
        )
        

        logger.info("Dataset profiling completed. rows: %d, columns: %d", rows, columns)
        
        
        return profile