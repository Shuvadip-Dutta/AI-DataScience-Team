import pandas as pd
from app.utils.logger import get_logger
from app.models.cleaning_report import CleaningReport


logger = get_logger(__name__)

class DataCleaner:
    """
    Cleans a dataset by handling missing values and duplicates.
    """
    def run(self, df: pd.DataFrame,) -> tuple[pd.DataFrame, CleaningReport]:
        """
        Clean the dataset and generate a cleaning report.
        """
        if df is None:
            raise ValueError("Input DataFrame cannot be None.")

        if df.empty:
            raise ValueError("Input DataFrame is empty.")

        logger.info("Starting dataset cleaning")
        
        rows_before = len(df)

        columns = len(df.columns)

        missing_before = int(df.isnull().sum().sum())
        
        cleaned_df = df.copy()
        
        duplicates_before = int(cleaned_df.duplicated().sum())

        cleaned_df = cleaned_df.drop_duplicates(inplace=False)
        
        numeric_columns = cleaned_df.select_dtypes(include="number").columns

        for column in numeric_columns:
            cleaned_df[column] = cleaned_df[column].fillna(
                cleaned_df[column].median()
            )
            
        categorical_columns = cleaned_df.select_dtypes(exclude="number").columns

        for column in categorical_columns:

            mode = cleaned_df[column].mode()

            if not mode.empty:
                cleaned_df[column] = cleaned_df[column].fillna(mode.iloc[0])
                
        rows_after = len(cleaned_df)
        missing_after = int(cleaned_df.isnull().sum().sum())
        
        report = CleaningReport(
            rows_before=rows_before,
            rows_after=rows_after,
            columns=columns,
            duplicate_rows_removed=duplicates_before,
            missing_values_before=missing_before,
            missing_values_after=missing_after,
        )
        
        logger.info(
            "Cleaning completed | rows_before=%d | rows_after=%d | duplicates_removed=%d | missing_before=%d | missing_after=%d",
            rows_before,
            rows_after,
            duplicates_before,
            missing_before,
            missing_after,
        )
        return cleaned_df, report